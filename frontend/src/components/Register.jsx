import React from 'react';
import '../assets/styles/style.css';
import styles from './Register.module.css';

function Register() {
  return (
    <div className='flex items-center justify-center h-screen'>
      <div className={styles.item}>
        <h1>Войдите или зарегистрируйтесь</h1>
        <span>чтобы пользоваться сервисом</span>
      </div>
    </div>
  );
}

export default Register;
