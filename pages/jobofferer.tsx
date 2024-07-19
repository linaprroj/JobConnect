import React from 'react';
import Layout from '../components/Layout';
import styles from '../styles/JobOfferer.module.css';

const JobOfferer: React.FC = () => {
  return (
    <Layout>
      <div className={styles.container}>
        <h1>Job Offerer Process</h1>
        <div className={styles.step}>Register</div>
        <div className={styles.step}>Create Profile</div>
        <div className={styles.step}>Post Job Opening</div>
        <div className={styles.step}>Receive Applications</div>
        <div className={styles.step}>Filter Applications</div>
        <div className={styles.step}>Select Candidates</div>
        <div className={styles.step}>Update Candidates</div>
        <div className={styles.step}>Extend Job Offers</div>
      </div>
    </Layout>
  );
};

export default JobOfferer;
