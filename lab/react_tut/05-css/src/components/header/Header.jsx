import React from 'react'
import styles from './Header.module.css'

const Header = () => {
  return (
    <div>
      <div className={styles.header}>
        <h3>Satyasish</h3>
        <button>Login</button>
      </div>
    </div>
  )
}

export default Header