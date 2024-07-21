import { NextPage } from "next";
import Header from "../../components/Header/Header";
import Link from "next/link";
import styles from "../../styles/HomePage.module.css";

const HomePage: NextPage = () => {
  return (
    <>
      <Header />
      <div className={styles.page}>
        <h1 className={styles.h1}>Welcome to JobConnect</h1>
        <p className={styles.p}>Connecting you with opportunities!</p>
        <div className={styles.button_styles}>
          <Link href="/joblist">
            <button className={styles.button}>JobSeeker</button>
          </Link>
          <Link href="/recruiter/dashboard">
            <button className={styles.button}>Recruiters</button>
          </Link>
        </div>
      </div>
    </>
  );
};

export default HomePage;







