import React from 'react';
import Navigation from '../../components/Navigation';
import './ArtDeco.css';

export default function ArtDeco() {
  return (
    <div className="art-deco-page">
      <Navigation title="Art Deco" description="Nafis, oltin chiziqlar, geometrik naqshlar" />
      <main className="deco-main">
        <div className="deco-border">
          <section className="deco-hero">
            <h1>Gatsby</h1>
            <p>1920-yillarning boyligi va nafosati. Simmetriya va oltin naqshlar.</p>
          </section>
        </div>
      </main>
    </div>
  );
}