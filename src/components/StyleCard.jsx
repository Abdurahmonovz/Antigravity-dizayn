import React from 'react';
import { Link } from 'react-router-dom';
import './StyleCard.css';

export default function StyleCard({ style }) {
  return (
    <Link to={style.path} className={`style-card ${style.previewClass}`}>
      <div className="card-preview">
        {/* Placeholder for a style-specific visual preview */}
        <div className="preview-content"></div>
      </div>
      <div className="card-info">
        <h3>{style.name}</h3>
        <p>{style.description}</p>
      </div>
    </Link>
  );
}
