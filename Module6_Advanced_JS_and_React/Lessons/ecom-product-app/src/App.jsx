import { useState } from 'react';
import ProductList from './components/ProductList';

function App() {
  const [products] = useState([
    {
      id: 1,
      name: 'Wireless Headphones',
      price: '$99.99',
      description: 'High-quality sound with noise cancellation.',
    },
    {
      id: 2,
      name: 'Smartwatch',
      price: '$149.99',
      description: 'Stay connected and track your fitness.',
    },
    {
      id: 3,
      name: 'Bluetooth Speaker',
      price: '$79.99',
      description: 'Portable speaker with excellent bass.',
    },
  ]);

  return (
    <div className="app">
      <h1 className="title">E-Commerce Product Listing</h1>
      <ProductList products={products} />
    </div>
  );
}

export default App;
