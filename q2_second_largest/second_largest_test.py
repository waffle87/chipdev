import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer


@cocotb.test()
async def test_second_largest(dut):
    clock = Clock(dut.clk, 10, unit="ns")
    cocotb.start_soon(clock.start())

    dut.resetn.value = 0
    await RisingEdge(dut.clk)
    dut.resetn.value = 1
    await RisingEdge(dut.clk)

    din1 = [0x2, 0x6, 0x0, 0xE, 0xC]
    dout1 = [0x0, 0x2, 0x2, 0x6, 0xC]

    for i, (din_val, expected) in enumerate(zip(din1, dout1)):
        dut.din.value = din_val
        await RisingEdge(dut.clk)
        await Timer(1, unit="ns")

        actual = dut.dout.value.to_unsigned()
        dut._log.info(
            f"pre-reset step {i + 1}: din = 0x{din_val:x}, dout = 0x{actual:x}, expected = 0x{expected:x}"
        )
        assert actual == expected, (
            f"mismatch at step {i + 1}: got 0x{actual:x}, expected 0x{expected:x}"
        )

    dut.resetn.value = 0
    await RisingEdge(dut.clk)
    dut.resetn.value = 1

    din2 = [0x0, 0x1, 0x2]
    dout2 = [0x0, 0x0, 0x1]

    for i, (din_val, expected) in enumerate(zip(din2, dout2)):
        dut.din.value = din_val
        await RisingEdge(dut.clk)
        await Timer(1, unit="ns")

        actual = dut.dout.value.to_unsigned()
        dut._log.info(
            f"post-reset step {i + 1}: din = 0x{din_val:x}, dout = 0x{actual:x}, expected = 0x{expected:x}"
        )
        assert actual == expected, (
            f"mismatch at step {i + 1}: got 0x{actual:x}, expected 0x{expected:x}"
        )
