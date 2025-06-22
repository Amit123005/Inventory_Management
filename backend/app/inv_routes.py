from flask import Blueprint, request, jsonify
from .models import Inventory
from icecream import ic

inventory_bp = Blueprint('inventory', __name__, url_prefix='/api')

@inventory_bp.route("/add_item", methods=["POST"])
def add_item():
    try:
        data = request.get_json()
        ic("Received item:", data)

        # Call your DB/service layer to add item
        result = Inventory.add_item(data)

        return jsonify({
            "status": "success",
            "message": "Item added successfully",
            "item": result  # you can return the added item or ID
        }), 201

    except Exception as e:
        ic("Error adding item:", e)
        return jsonify({
            "status": "error",
            "message": "Failed to add item",
            "error": str(e)
        }), 500
    
@inventory_bp.route("/items", methods=["GET"])
def get_items():
    try:
        result = Inventory.view_item()
        return jsonify({"items": result}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500