CONTIKI_PROJECT = sender coordinator
all: $(CONTIKI_PROJECT)

PLATFORMS_EXCLUDE = sky nrf52dk native simplelink

CONTIKI=../..

TARGET = iotlab
BOARD = m3
ARCH_PATH=../../../arch

MAKE_MAC = MAKE_MAC_TSCH

include $(CONTIKI)/Makefile.dir-variables
MODULES += $(CONTIKI_NG_SERVICES_DIR)/shell
MODULES += $(CONTIKI_NG_SERVICES_DIR)/orchestra

include $(CONTIKI)/Makefile.include
