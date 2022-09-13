import type { NextPage } from 'next'
import { useEffect, useState } from 'react';
import styles from '../styles/Home.module.css'

const Home: NextPage = () => {
  const [message, setMessage] = useState(null);
  
  useEffect(() => {
    fetch('/api/')
      .then((res) => res.json())
      .then((data) => {
        setMessage(data.message)
      })
  }, [])

  return (
    <div className={styles.container}>
      {message}
    </div>
  )
}

export default Home
