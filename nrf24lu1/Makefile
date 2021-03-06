# Copyright 2017 jem@seethis.link
# Licensed under the MIT license (http://opensource.org/licenses/MIT)

#######################################################################
#                        global build defines                         #
#######################################################################

TARGET_BASE_NAME = keyplus_nrf24lu1
OBJ_DIR	= obj
MCU		= NRF24LU1
F_CPU	= 16000000
MCU_STRING = nRF24LU1P_F32

# valid 16 or 32
FLASH_SIZE = 32

KEYPLUS_PATH = ../src

USE_USB := 1
USE_NRF24 := 1
USE_I2C := 0
USE_SCANNER := 0

KEYPLUS_CLI = ../host-software/keyplus-cli

# Prototype IDs
# USB_VID = 6666
# USB_PID = 3333

USB_VID = 1209
USB_PID = BB02

#######################################################################
#                               config                                #
#######################################################################

include scripts/boards.mk

ifndef ID
  ID=0
endif

ifndef LAYOUT_FILE
  LAYOUT_FILE=../layouts/basic_split_test.yaml
endif

ifndef RF_FILE
  RF_FILE=../layouts/test_rf_config.yaml
endif

#######################################################################
#                            source files                             #
#######################################################################

C_SRC += \
	aes.c \
	flash.c \
	hardware.c \
	led.c \
	main.c \
	nonce.c \
	nrf24.c \
	timer.c \
	usb.c \
	usb_reports.c \
	descriptors.c \


ASM_SRC = \
	crtxinit.S \


include $(KEYPLUS_PATH)/core/core.mk
include $(KEYPLUS_PATH)/usb/usb.mk
include $(KEYPLUS_PATH)/key_handlers/key_handlers.mk

#######################################################################
#                              c defines                              #
#######################################################################

VPATH += $(KEYPLUS_PATH)

INC_PATHS += \
	-I. \
	-I$(KEYPLUS_PATH) \

CDEFS += \
	-D$(MCU) \
	-DINTEL_8052 \
	-DNO_RF_TRANSMIT \
	-DF_CPU=$(F_CPU)UL \

CDEFS += -DUSB_BUFFERED=0

ifdef DEBUG_LEVEL
	CDEFS += -DDEBUG_LEVEL=$(DEBUG_LEVEL)
endif

#######################################################################
#                     flash and storage settings                      #
#######################################################################

CDEFS += -DFLASH_$(FLASH_SIZE)

#######################################################################
#                     linker and compiler options                     #
#######################################################################

# Using optimize for speed can result in a smaller binary in sdcc
OPTIMIZATION = --opt-code-speed
# OPTIMIZATION = --opt-code-size


# Version of sdcc used:
# /usr/local/bin/sdcc --version
# SDCC : mcs51/z80/z180/r2k/r3ka/gbz80/tlcs90/ds390/pic16/pic14/TININative/ds400/hc08/s08/stm8 3.6.8 #9948 (Linux)

SDCC_PATH = /usr/local/bin
AS = $(SDCC_PATH)/sdas8051
CC = $(SDCC_PATH)/sdcc
PP = $(SDCC_PATH)/sdcpp

# SDCC_PATH = /usr/bin
# AS = $(SDCC_PATH)/sdas8051
# CC = $(SDCC_PATH)/sdcc
# PP = $(SDCC_PATH)/sdcpp

CFLAGS   = \
	$(CDEFS) \
	$(INC_PATHS) \
	$(OPTIMIZATION) \
	--fomit-frame-pointer \
	--model-small \
	# --stack-auto \
	# --Werror \
	# --model-small \
	# --code-movx \
	# --disable-warning 85 \
	# --model-large \
	#

LFLAGS   = \
	--code-loc 0x0000 \
	--code-size $(CODE_SIZE) \
	--xram-loc 0x8000 \
	--xram-size 0x800 \
	--iram-size 0x100 \
	--stack-loc 0x080 \
	--stack-size 0x060 \
	# --parms-in-bank1

ASFLAGS  = -xglospff

# see the boards directory for these definitions
CDEFS += -DSETTINGS_ADDR=$(SETTINGS_ADDR)
CDEFS += -DLAYOUT_ADDR=$(LAYOUT_ADDR)
CDEFS += -DLAYOUT_SIZE=$(LAYOUT_SIZE)
CDEFS += -DNONCE_ADDR=$(NONCE_ADDR)
CDEFS += -DBOOTLOADER_ADDR=$(BOOTLOADER_ADDR)

#######################################################################
#                               recipes                               #
#######################################################################

C_REL_FILES = $(patsubst %.c, $(OBJ_DIR)/%.rel, $(C_SRC))
ASM_REL_FILES = $(patsubst %.S, $(OBJ_DIR)/%.rel, $(ASM_SRC))
DEP_FILES = $(patsubst %.c, $(OBJ_DIR)/%.dep, $(C_SRC))
REL_FILES = $(C_REL_FILES) $(ASM_REL_FILES)

LAYOUT_NAME=$(basename $(notdir $(LAYOUT_FILE)))
MERGED_HEX="$(BUILD_TARGET_DIR)/$(basename $(TARGET))-$(LAYOUT_NAME).hex"

all: $(TARGET_HEX) $(MERGED_HEX) size

$(TARGET_HEX): $(DEP_FILES) $(REL_FILES)
	@echo "=== compiling target ==="
	$(CC) --version
	$(CC) $(CFLAGS) $(LFLAGS) $(REL_FILES) -o $@
	# @mv *.lk *.map *.mem -t $(OBJ_DIR)

$(MERGED_HEX): $(TARGET_HEX) $(BOOTLOADER)
	@echo "=== appending bootloader ==="
	sed '/^:00000001FF/d' $(TARGET_HEX) > $(TARGET_HEX)_with_bootloader.hex
	cat $(BOOTLOADER) >> $(TARGET_HEX)_with_bootloader.hex
	echo ':00000001FF' >> $(TARGET_HEX)_with_bootloader.hex
# sort the hex for easier inspection
	@echo "=== merging layout settings files ==="
	$(KEYPLUS_CLI) program \
		$(KEYPLUS_CLI_LAYOUT_FLAGS) \
		--new-id $(ID) \
		--layout $(LAYOUT_FILE) \
		--rf $(RF_FILE) \
		--fw-hex $(TARGET_HEX)_with_bootloader.hex \
		-M $(SETTINGS_ADDR) $(LAYOUT_ADDR) $(LAYOUT_SIZE) \
		-o $(BUILD_TARGET_DIR)/$(TARGET)-$(LAYOUT_NAME).hex \
		-F scan_method=none \
		-F chip_name=nRF24LU1P-F32 \

size: $(TARGET_HEX)
	@echo "=== Size Information ($(TARGET))==="
	@scripts/hex-size.sh $< $(BUILD_TARGET_DIR)/$(TARGET).mem

# rule for c
$(OBJ_DIR)/%.rel: %.c
	@echo "compiling: $<"
	@mkdir -p $(dir $@)
	@$(CC) $(CFLAGS) -c $< -o $@

# rule for asm
$(OBJ_DIR)/%.rel: %.S
	@mkdir -p $(dir $@)
	$(AS) $(ASFLAGS) $@ $<

# rule for DEP_FILES
# sdcc doesn't pass the -MT flag correctly to the preprocessor, so need to
# call the preprocessor directly to generate dependency files
$(OBJ_DIR)/%.dep: %.c
	@mkdir -p $(dir $@)
	@$(PP) $(INC_PATHS) $(CDEFS) -MM -MT $(basename $@).rel $< -o $@

clean:
	rm -f $(BUILD_TARGET_DIR)/*.hex
	rm -f $(BUILD_TARGET_DIR)/*.lk
	rm -f $(BUILD_TARGET_DIR)/*.map
	rm -f $(BUILD_TARGET_DIR)/*.mem
	rm -fr $(OBJ_DIR)
	rm -fr nrfburn.txt

program-boot: $(MERGED_HEX) size
	$(KEYPLUS_CLI) bootloader -p $(MCU_STRING) | sleep 1.0
	./nrf24lu1p-512-bootloader/scripts/flash.py write_hex $<

program-unirecv: $(MERGED_HEX)
	$(KEYPLUS_CLI) bootloader -p $(MCU_STRING) | sleep 1.0
	../host-software/uniflash/uniflash.py flash $<

program-hard:: $(MERGED_HEX) size
	./scripts/strip_chip_id.sh $(MERGED_HEX) > $(MERGED_HEX)_no_chip_id.hex
	nrfburn -f $(FLASH_SIZE) -w $(MERGED_HEX)_no_chip_id.hex


version:
	$(CC) --version

-include $(DEP_FILES)

.PHONY: clean flash program all size version
