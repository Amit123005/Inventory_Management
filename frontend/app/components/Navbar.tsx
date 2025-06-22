import { AppBar, Box, Button, Toolbar, Typography } from "@mui/material";
import { Link, useLocation } from "react-router";

export default function Navbar() {
  const location = useLocation();

  const navLinks = [
    { to: "/", label: "Home" },
    { to: "/add", label: "Add Item" },
    { to: "/view", label: "View Items" },
  ];

  return (
    <AppBar position="static" color="primary">
      <Toolbar>
        <Typography variant="h6" sx={{ flexGrow: 1 }}>
          Inventory App
        </Typography>
        <Box>
          {navLinks.map((link) => (
            <Button
              key={link.to}
              component={Link}
              to={link.to}
              color="inherit"
              sx={{
                textTransform: "none",
                fontWeight: location.pathname === link.to ? "bold" : "normal",
                borderBottom: location.pathname === link.to ? "2px solid white" : "none",
                borderRadius: 0,
              }}
            >
              {link.label}
            </Button>
          ))}
        </Box>
      </Toolbar>
    </AppBar>
  );
}
