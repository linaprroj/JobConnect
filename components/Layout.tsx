import React, { ReactNode } from 'react';
import Navbar from './Navbar';
import styles from '../styles/Layout.module.css';

interface LayoutProps {
  children: ReactNode;
}

const Layout: React.FC<LayoutProps> = ({ children }) => {
  return (
    <>
      <Navbar />
      <div className={styles.container}>
        <main className={styles.main}>
          {children}
        </main>
      </div>
    </>
  );
};

export default Layout;

