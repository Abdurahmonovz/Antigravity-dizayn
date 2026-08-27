import React from 'react';
import Navigation from '../../components/Navigation';
import './Bauhaus.css';

export default function Bauhaus() {
  return (
    <div className="bauhaus-page">
      <Navigation title="Bauhaus" description="Asosiy geometrik shakllar, asosiy ranglar" />
      <main className="bh-main">
        <section className="bh-hero">
          <div className="bh-shape bh-circle"></div>
          <div className="bh-shape bh-square"></div>
          <div className="bh-shape bh-triangle"></div>
          <div className="bh-hero-content">
            <h1>BAUHAUS</h1>
            <p>Form follows function. Dizayn arxitekturaga aylanadi.</p>
          </div>
        </section>
      </main>
    </div>
  );
}