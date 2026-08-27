import React from 'react';
import Navigation from '../../components/Navigation';
import './BentoGrid.css';

export default function BentoGrid() {
  return (
    <div className="bento-page">
      <Navigation title="Bento Grid" description="Bento qutisi kabi tartibli bloklar" />
      <main className="bento-main">
        <div className="bento-grid-container">
          <div className="bento-item hero-item">
            <h1>Bento UI</h1>
            <p>Ma'lumotlarni ixcham va vizual tartibda yetkazish usuli.</p>
          </div>
          <div className="bento-item image-item">Surat</div>
          <div className="bento-item stat-item">
            <h2>99%</h2>
            <p>Samaradorlik</p>
          </div>
          <div className="bento-item wide-item">Yana bir muhim xabar</div>
          <div className="bento-item square-item">A</div>
          <div className="bento-item square-item">B</div>
        </div>
      </main>
    </div>
  );
}