##############################################################
#
# GPIO-PACKAGE
#
##############################################################

#TODO: Fill up the contents below in order to reference your assignment 3 git contents
GPIO_PACKAGE_VERSION = 9bdd1c50c3a2f9d1428ea7bb734c597e671a1c46
# Note: Be sure to reference the *ssh* repository URL here (not https) to work properly
# with ssh keys and the automated build/test system.
# Your site should start with git@github.com:
GPIO_PACKAGE_SITE = git@github.com:cu-ecen-aeld/final-project-Amey2904dash.git
GPIO_PACKAGE_SITE_METHOD = git
GPIO_PACKAGE_GIT_SUBMODULES = YES

define GPIO_PACKAGE_BUILD_CMDS
	$(MAKE) $(TARGET_CONFIGURE_OPTS) -C $(@D)/sample_socket/socket_client all
endef

# TODO add your writer, finder and finder-test utilities/scripts to the installation steps below
define GPIO_PACKAGE_INSTALL_TARGET_CMDS
	$(INSTALL) -m 0755 $(@D)/sample_socket/socket_client/socket_client $(TARGET_DIR)/usr/bin
endef

$(eval $(generic-package))
