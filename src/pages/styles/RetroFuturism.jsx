import React from 'react';
import Navigation from '../../components/Navigation';
import './RetroFuturism.css';

export default function RetroFuturism() {
  return (
    <div className="retro-page">
      <Navigation title="Retro-Futurism" description="60-70-yillar kelajak tasavvuri" />
      <main className="retro-main">
        <section className="retro-hero">
          <h1>SPACE AGE</h1>
          <p>Yumshoq pastel ranglar va qalin yumaloq shriftlar.</p>
          <div className="retro-circles">
            <div className="circle c1"></div>
            <div className="circle c2"></div>
            <div className="circle c3"></div>
          </div>
        </section>
      </main>
    </div>
  );
}