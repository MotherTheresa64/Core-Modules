from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

from app.schemas import UserSchema, ProductSchema, OrderSchema

print("Schemas loaded:", UserSchema, ProductSchema, OrderSchema)
