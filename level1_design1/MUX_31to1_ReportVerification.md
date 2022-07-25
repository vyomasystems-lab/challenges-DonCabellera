# L1_D1: MUX 31 to 1 Verification Report.
The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

The first challenge design is a multiplexer with 31 inputs and 1 output. All of the inputs are controlled by a Selector, which is a 5 bit word. The bus input carries 2 bits, so the output. The test I made can be seen above:

```sh
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
```

With this test we can see how the input is selected by the variable "sel" and becomes the output of the system. Is an easy and short form, and it would be best to try the inputs randomly in a "for" loop.

![MuxTest](https://i.imgur.com/JY2XaXA.png)

## Verification Environment

 The test drives inputs to the Design Under Test (MUX31 to 1) which takes in 2-bit inputs *inp*[0-30] and gives 2-bit output *out*, selected by a 5-bit word named *sel*.

The values are assigned to the input port using 
```
dut.inp0.value = 1
dut.inp1.value = 3
···
```
The test of *mux.v* passed:
![Test Passed](https://i.imgur.com/7LFqt9F.png)

## Test Scenario
- Test Inputs: 
    ->imp0 = 01; 
    ->sel = 00000;
- Expected Output: out = 01;

## Design Bug
Based on the above test input and analysing the design, we see the following. The fisrt Bug we can perceive, ocurrs when the inputs is out of range.
### Bug 1: 
```
#Assign a value out of the 2-bit range:
dut.inp0.value = 9 ===========>BUG
```
![Error1](https://i.imgur.com/QWxp0Tz.png)
### Solution:
As a hardware design, if we have a bus or signal connected with more bits than required we will lose information. To fix this bug we must pay atention to the buses connectors between modules. Or just make a standard width bus, which support every bit traffic.

### Bug 2:
```
#Asignamos un valor a un input
dut.inp31.value = 1 ===========>BUG
```
![Error2](https://i.imgur.com/2ztcLV9.png)
### Solution:
Moreover, as the number inputs of the multiplexer is just 31, if we choose a 32 option with *sel*, system will crush. The solution is to contemplate the last option, and if it is ever selected, output get a 0 (0 volt).

## Verification Strategy
In this challenge, I used the Traditional Verification, but is advisable to test it with Constrained Random Verification to improve the practice.

## Is the verification complete ?
Yes
