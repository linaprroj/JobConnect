import React from 'react';
import Layout from '../components/Layout';
import styles from '../styles/JobSeeker.module.css';

const JobSeeker: React.FC = () => {
  return (
    <Layout>
      <div className={styles.container}>
        <h1>Job Seeker Process</h1>
        <div className={styles.step}>Register</div>
        <div className={styles.step}>Create Profile</div>
        <div className={styles.step}>Search Jobs</div>
        <div className={styles.step}>Find Job Posting</div>
        <div className={styles.step}>Upload Resume</div>
        <div className={styles.step}>Submit Application</div>
        <div className={styles.step}>Receive Email Confirmation</div>
        <div className={styles.step}>Track Application</div>
      </div>
    </Layout>
  );
};

export default JobSeeker;
