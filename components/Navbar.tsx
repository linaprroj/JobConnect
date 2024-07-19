import React from 'react';
import Link from 'next/link';
import styles from '../styles/Navbar.module.css';

const Navbar: React.FC = () => {
  return (
    <nav className={styles.navbar}>
      <Link href="/">Home</Link>
      <Link href="/jobseeker">Job Seeker</Link>
      <Link href="/jobofferer">Job Offerer</Link>
    </nav>
  );
};

export default Navbar;