##############################################################
#
# GPIO-PACKAGE
#
##############################################################

#TODO: Fill up the contents below in order to reference your assignment 3 git contents
GPIO_PACKAGE_VERSION = 3d54e0f14446d055ee69f0b9c171d1fc9bbfa9f7
# Note: Be sure to reference the *ssh* repository URL here (not https) to work properly
# with ssh keys and the automated build/test system.
# Your site should start with git@github.com:
GPIO_PACKAGE_SITE = git@github.com:cu-ecen-aeld/final-project-Amey2904dash.git
GPIO_PACKAGE_SITE_METHOD = git
GPIO_PACKAGE_GIT_SUBMODULES = YES

define GPIO_PACKAGE_BUILD_CMDS
	$(MAKE) $(TARGET_CONFIGURE_OPTS) -C $(@D)/gpio all
endef

# TODO add your writer, finder and finder-test utilities/scripts to the installation steps below
define GPIO_PACKAGE_INSTALL_TARGET_CMDS
	$(INSTALL) -m 0755 $(@D)/gpio/lcd $(TARGET_DIR)/usr/bin
endef

$(eval $(generic-package))
