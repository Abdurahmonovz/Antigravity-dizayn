import React from 'react';
import Navigation from '../../components/Navigation';
import './VaporwaveY2k.css';

export default function VaporwaveY2k() {
  return (
    <div className="vw-page">
      <Navigation title="Vaporwave / Y2K" description="Neon pushti-binafsha gradientlar, retro-futuristik grafika" />
      <div className="vw-sun"></div>
      <div className="vw-grid"></div>
      <main className="vw-main">
        <section className="vw-hero">
          <h1 className="glitch" data-text="A E S T H E T I C">A E S T H E T I C</h1>
          <p>Windows 95, neon quyoshlar va nostalgiya hissiyoti.</p>
        </section>

        <section className="vw-cards">
          <div className="vw-card">
            <h2>Nostalgiya</h2>
            <p>Eski texnologiyalar va 90-yillar romantikasi.</p>
          </div>
          <div className="vw-card">
            <h2>Neon Gradientlar</h2>
            <p>Pushti, binafsha va havorang neon chiziqlar.</p>
          </div>
        </section>
      </main>
    </div>
  );
}