import React from 'react';
import { Link } from 'react-router-dom';
import { ArrowLeft } from 'lucide-react';
import './Navigation.css';

export default function Navigation({ title, description }) {
  return (
    <nav className="style-nav">
      <Link to="/" className="nav-back">
        <ArrowLeft size={20} />
        Orqaga
      </Link>
      <div className="nav-badge">
        <span className="badge-title">{title}</span>
        <span className="badge-desc">{description}</span>
      </div>
    </nav>
  );
}
