import React from 'react';
import Navigation from '../../components/Navigation';
import './MemphisDesign.css';

export default function MemphisDesign() {
  return (
    <div className="memphis-page">
      <Navigation title="Memphis Design" description="80-yillar uslubi, geometrik shakllar, to'q ranglar" />
      <main className="memphis-main">
        <div className="memphis-shape shape-1"></div>
        <div className="memphis-shape shape-2"></div>
        <div className="memphis-shape shape-3"></div>
        
        <section className="memphis-hero">
          <h1>MEMPHIS 80s</h1>
          <p>Yorqin, qarama-qarshi ranglar va mavhum geometrik shakllarning erkin uyg'unligi.</p>
        </section>

        <section className="memphis-cards">
          <div className="memphis-card">
            <div className="memphis-icon circle"></div>
            <h2>Geometriya</h2>
            <p>Doiralar, uchburchaklar va zigzag chiziqlar.</p>
          </div>
          <div className="memphis-card">
            <div className="memphis-icon square"></div>
            <h2>Naqshlar</h2>
            <p>Nuqtalar, panjaralar va qora-oq naqshlar asosiysi.</p>
          </div>
          <div className="memphis-card">
            <div className="memphis-icon triangle"></div>
            <h2>Pop Ranglar</h2>
            <p>Neon va qattiq ranglarning kuchli kontrasti.</p>
          </div>
        </section>
      </main>
    </div>
  );
}