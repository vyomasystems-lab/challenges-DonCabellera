# See LICENSE.vyoma for details

TOPLEVEL_LANG ?= Systemverilog

PWD=$(shell pwd)

VERILOG_SOURCES = $(PWD)/patternMoorev.v 	# provide your design path

TOPLEVEL := patternMoorev 				# design file
MODULE   := test_patternMoorev				# test file

include $(shell cocotb-config --makefiles)/Makefile.sim

clean_all: clean
	rm -rf *.xml sim_build __pycache__ 
