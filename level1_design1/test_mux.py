# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    dut.log.info('####### CTB: mine test :########')

    #Asignamos un valor a un input
    dut.inp0.value = 1

    dut.inp1.value = 3
    # dut.inp2.value = 0
    # dut.inp3.value = 2
    # dut.inp4.value = 0
    
    #Asignamos el valor de la entrada al selector del MUX
    dut.sel.value = 0

    #Agregamos el Timer de 2 ns para que el mux setee los valores. (Agregar sino no funciona.)
    await Timer(2,units='ns')
    
    #Imprimimos en el Log los valores de Entrada - Salida
    dut._log.info("\n########## VALORES ########## \n")
    dut._log.info("DUT ->  \nINP0= {} \nSEL= {}\nOUT= {}\n".format(dut.inp0.value, dut.sel.value, dut.out.value))

    dut._log.info("Test terminado. Luciano")

    