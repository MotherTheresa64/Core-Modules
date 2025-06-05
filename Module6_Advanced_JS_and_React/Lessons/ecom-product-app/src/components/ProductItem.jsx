function ProductItem({ product }) {
  return (
    <div className="product-item">
      <h2>{product.name}</h2>
      <p className="price">{product.price}</p>
      <p className="description">{product.description}</p>
    </div>
  );
}

export default ProductItem;
