import React from "react";
import {
  AppBar,
  IconButton,
  Toolbar,
  Typography,
  Menu,
  MenuItem
} from "@mui/material";

import { AccountCircle } from '@mui/icons-material';
import { ownerProfile } from "./UserPosts.js";
import { ClickableCopyToClipboard } from "./utils/misc.js";

export const NavBarMenu = (ownerId: ownerProfile) => {
  const [anchorEl, setAnchorEl] = React.useState<null | HTMLElement>(null);

  const compactAccountMenu = (event: React.MouseEvent<HTMLElement>) => {
    setAnchorEl(event.currentTarget);
  }

  const handleClose = () => {
    setAnchorEl(null);
  };
  
  const accountDetailsSection = (isLoggedIn: Boolean) => {
    if (isLoggedIn) {
      return (<div>
        <IconButton
          size="large"
          aria-label="account of current user"
          aria-controls="menu-appbar"
          aria-haspopup="true"
          onClick={compactAccountMenu}
          color="inherit"
        >
          <AccountCircle />
        </IconButton>
        <Menu
          id="menu-appbar"
          anchorEl={anchorEl}
          anchorOrigin={{
            vertical: 'top',
            horizontal: 'right',
          }}
          keepMounted
          transformOrigin={{
            vertical: 'top',
            horizontal: 'right',
          }}
          open={Boolean(anchorEl)}
          onClose={handleClose}
        >
          <MenuItem onClick={handleClose}>Owner ID: {ownerId.ownerId} <ClickableCopyToClipboard {...ownerId}/></MenuItem>
          <MenuItem onClick={handleClose}>Total ToDos: 100000</MenuItem>
        </Menu>
      </div>)
    }
    return <div></div>
  };

  return (
          <AppBar position="static">
            <Toolbar>
              <Typography variant="h4" component="div" sx={{ flexGrow: 1 }}>
                Moehs ToDo App 🚀
              </Typography>
                {accountDetailsSection(ownerId.ownerId != "")}
            </Toolbar>
          </AppBar>)
}