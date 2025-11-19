import cocotb
from cocotb.triggers import Timer


@cocotb.test()
async def test_router(dut):
    def check_outputs(expected_values, step_desc):
        dut._log.info(step_desc)
        for i in range(4):
            expected = expected_values[i]
            actual = getattr(dut, f"dout{i}").value.to_unsigned()
            assert actual == expected, (
                f"dout{i}: got 0x{actual:x}, expected 0x{expected:x}"
            )

    dut.addr.value = 0x1
    dut.din_en.value = 1
    dut.din.value = 0xBEE
    dout1 = [0x0, 0xBEE, 0x0, 0x0]
    await Timer(1, unit="ns")
    check_outputs(dout1, "state 1: addr = 1, din_en = 1, din = 0xBEE, dout1 = 0xBEE")

    dut.addr.value = 0x3
    dout2 = [0x0, 0x0, 0x0, 0xBEE]
    await Timer(1, unit="ns")
    check_outputs(dout2, "state 2: addr = 3, din_en = 1, din = 0xBEE, dout3 = 0xBEE")

    dut.din_en.value = 0
    dout3 = [0x0, 0x0, 0x0, 0x0]
    await Timer(1, unit="ns")
    check_outputs(
        dout3, "state 3: addr = 3, din_en = 0, din = 0xBEE, dout{0,1,2,3} = 0"
    )
