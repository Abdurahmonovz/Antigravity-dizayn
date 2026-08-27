import React from 'react';
import Navigation from '../../components/Navigation';
import './AuroraGradientMesh.css';

export default function AuroraGradientMesh() {
  return (
    <div className="aurora-page">
      <div className="aurora-bg"></div>
      <Navigation title="Aurora" description="Yumshoq gradientlar va organik shakllar" />
      <main className="aurora-main">
        <section className="aurora-glass">
          <h1>Gradient Mesh</h1>
          <p>Yorug'lik nurlari kabi o'zgaruvchi va oqib o'tuvchi yumshoq ranglar.</p>
        </section>
      </main>
    </div>
  );
}