#
# Copyright (c) 2015 Arduino Srl. All right reserved.
#
# This is free software, licensed under the GNU General Public License v2.
# See /LICENSE for more information.
#

include $(TOPDIR)/rules.mk

PKG_CONNECTOR:=smtp
PKG_NAME:=ciao-connector-$(PKG_CONNECTOR)
PKG_REVISION:=<HASH>
PKG_VERSION:=0.0.1
PKG_RELEASE:=1
PKG_INST_DIR:=/root/.ciao
PKG_CONF_DIR:=/usr/lib/python2.7/ciao/conf
PKG_REPO_NAME:=arduino-ciao-$(PKG_CONNECTOR)-connector
PKG_REPO_USERNAME:=arduino-org

PKG_SOURCE_PROTO:=git

PKG_SOURCE:=$(PKG_NAME)-$(PKG_REVISION).tar.gz
PKG_SOURCE_URL:=https://github.com/$(PKG_REPO_USERNAME)/$(PKG_REPO_NAME).git
PKG_SOURCE_VERSION:=$(PKG_REVISION)
PKG_SOURCE_SUBDIR:=$(PKG_NAME)-$(PKG_REVISION)

PKG_BUILD_DIR:=$(BUILD_DIR)/$(PKG_NAME)-$(PKG_REVISION)

include $(INCLUDE_DIR)/package.mk

define Package/ciao-$(PKG_CONNECTOR)
  SECTION:=utils
  CATEGORY:=Utilities
  TITLE:=Arduino Ciao $(PKG_CONNECTOR) Connector
  DEPENDS:=+python +python-mini +ciao
endef

define Package/ciao-$(PKG_CONNECTOR)/description
    Arduino Ciao - $(PKG_CONNECTOR) client connector library.
endef

define Build/Compile
    # NOOP
endef

define Package/ciao-$(PKG_CONNECTOR)/install
    $(INSTALL_DIR) $(1)$(PKG_INST_DIR)/$(PKG_CONNECTOR)
    $(INSTALL_DATA) $(PKG_BUILD_DIR)/$(PKG_CONNECTOR)/$(PKG_CONNECTOR).json.conf $(1)$(PKG_INST_DIR)/$(PKG_CONNECTOR)
		$(INSTALL_BIN) $(PKG_BUILD_DIR)/$(PKG_CONNECTOR)/*.py $(1)$(PKG_INST_DIR)/$(PKG_CONNECTOR)

    $(INSTALL_DIR) $(1)$(PKG_CONF_DIR)
    $(INSTALL_DATA) $(PKG_BUILD_DIR)/$(PKG_CONNECTOR).json.conf $(1)$(PKG_CONF_DIR)
endef

$(eval $(call BuildPackage,ciao-$(PKG_CONNECTOR)))
