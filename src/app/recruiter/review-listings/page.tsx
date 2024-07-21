"use client";

import React from "react";
import Header from "../../../../components/Header/Header";
import styles from "../../../../styles/RecruiterReviewListings.module.css";

const sampleJobs = [
  {
    id: 1,
    title: "Software Engineer",
    company: "Google",
    location: "New York",
    salary: "157,000",
  },
  {
    id: 2,
    title: "Marketing Specialist",
    company: "Uniqlo",
    location: "Los Angeles",
    salary: "77,000",
  },
  {
    id: 3,
    title: "Data Scientist",
    company: "OpenAI",
    location: "San Francisco",
    salary: "127,000",
  },
];

const RecruiterReviewListings: React.FC = () => {
  const handleReviewCandidates = (jobId: number) => {
    console.log("Review candidates for job:", jobId);
  };

  const handleDeleteListing = (jobId: number) => {
    console.log("Delete listing for job:", jobId);
  };

  return (
    <div className={styles.page}>
      <Header />
      <h1 className={styles.title}>Your Job Listings</h1>
      <div className={styles.jobList}>
        {sampleJobs.map((job) => (
          <div key={job.id} className={styles.jobCard}>
            <h2>{job.title}</h2>
            <p>Company: {job.company}</p>
            <p>Location: {job.location}</p>
            <p>Salary: ${job.salary}</p>
            <div className={styles.buttonContainer}>
              <button className={styles.button} onClick={() => handleReviewCandidates(job.id)}>
                Review Candidates
              </button>
              <button className={styles.button} onClick={() => handleDeleteListing(job.id)}>
                Delete Listing
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default RecruiterReviewListings;


