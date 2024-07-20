import { NextPage } from "next";
import JobCard from "../../../components/JobCard/JobCard";
import styles from "../../../styles/joblist/joblist.module.css";

const JobListPage: NextPage = () => {
  const dummyJobs = [
    {
      title: "Software Engineer",
      company: "Google",
      location: "New York",
      salary: "157,000",
    },
    {
      title: "Marketing Specalist",
      company: "Uniqlo",
      location: "Los Angeles",
      salary: "77,000",
    },
    {
      title: "Data Scientist",
      company: "OpenAI",
      location: "San Franscisco",
      salary: "127,000",
    },
    {
      title: "Software Engineer",
      company: "Google",
      location: "New York",
      salary: "157,000",
    },
    {
      title: "Marketing Specalist",
      company: "Uniqlo",
      location: "Los Angeles",
      salary: "77,000",
    },
    {
      title: "Data Scientist",
      company: "OpenAI",
      location: "San Franscisco",
      salary: "127,000",
    },
  ];
  return (
    <div className={styles.page}>
      <h1 style={{ marginLeft: "2rem" }}>Job Listings</h1>
      <div className={styles.job_container}>
        {dummyJobs.map((job) => (
          <div key={Math.random()} className={styles.jobcard}>
            <JobCard
              title={job.title}
              company={job.company}
              location={job.location}
              salary={job.salary}
            />
          </div>
        ))}
      </div>
    </div>
  );
};

export default JobListPage;