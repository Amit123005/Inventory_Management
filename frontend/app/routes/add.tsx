import { Box, Button, Container, MenuItem, TextField, Typography,} from "@mui/material";
import { useState } from "react";

export default function Add() {
  const [item, setItem] = useState({
    name: "",
    category: "",
    quantity: 1,
  });

  const handleChange = (
    e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>
  ) => {
    const { name, value } = e.target;
    setItem((prev) => ({
      ...prev,
      [name]: name === "quantity" ? parseInt(value) : value,
    }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
  e.preventDefault();

  try {
    const response = await fetch("http://192.168.29.38:5000/api/add_item", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(item),
    });

    if (!response.ok) {
      throw new Error(`Failed to add item: ${response.statusText}`);
    }

    const data = await response.json();
    console.log("Server response:", data);
    alert("Item added successfully!");

    // Reset form
    setItem({ name: "", category: "", quantity: 1 });
  } catch (error) {
    console.error("Error submitting item:", error);
    alert("Failed to add item. Please try again.");
  }
};


  return (
    <Container maxWidth="sm" sx={{ mt: 8 }}>
      <Typography variant="h4" gutterBottom>
        Add New Item
      </Typography>

      <Box component="form" onSubmit={handleSubmit} sx={{ display: "flex", flexDirection: "column", gap: 2 }}>
        <TextField
          label="Item Name"
          name="name"
          value={item.name}
          onChange={handleChange}
          required
        />

        <TextField
          select
          label="Category"
          name="category"
          value={item.category}
          onChange={handleChange}
          required
        >
          <MenuItem value="">Select category</MenuItem>
          <MenuItem value="Electronics">Electronics</MenuItem>
          <MenuItem value="Stationery">Stationery</MenuItem>
          <MenuItem value="Furniture">Furniture</MenuItem>
        </TextField>

        <TextField
          label="Quantity"
          name="quantity"
          type="number"
          value={item.quantity}
          onChange={handleChange}
          inputProps={{ min: 1 }}
          required
        />

        <Button type="submit" variant="contained" color="primary">
          Add Item
        </Button>
      </Box>
    </Container>
  );
}
