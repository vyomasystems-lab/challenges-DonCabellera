#This is the TestBEnch for the Machine "Alyssa’s snail"

import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def test_patternMoorev(dut):

    dut.log.info('#######   Test start:   ########')

    #Set the clock:
    clock = Clock(dut.clk, 10, units="ns")  # Create a 10ns period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    #Must reset first:
    dut.reset.value = 1
    await RisingEdge(dut.clk)  
    dut.reset.value = 0
    await RisingEdge(dut.clk)

    #Input
    dut.a.value = 1

    #Agregamos el Timer de 2 ns para que el mux setee los valores. (Agregar sino no funciona.)
    await Timer(2,units='ns')
    
    #Imprimimos en el Log los valores de Entrada - Salida
    dut._log.info("\n########## VALORES ########## \n")
    dut._log.info("DUT ->  \nINP0= {} \nOUT= {}\n".format(dut.a.value, dut.y.value, ))

    dut._log.info("Test terminado. Luciano")
