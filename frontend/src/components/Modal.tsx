import React from 'react';
import {motion} from "framer-motion";

interface ModalProps {
  active: boolean
  setActive: Function
  children: React.ReactNode
}

const Modal: React.FC<ModalProps> = ({children, active, setActive}) => {
  return (
    <motion.div
      className={'absolute inset-0 h-full w-full grid place-items-center bg-black bg-opacity-70'}
      initial={{opacity: 0}}
      onClick={() => setActive(false)}
      animate={{opacity: 1}}
      exit={{opacity: 0}}
    >
      <div
        className='w-11/12 bg-zinc-800 rounded-2xl text-white modal:w-96 absolute'
        onClick={(e => e.stopPropagation())}
      >
        {children}
      </div>
    </motion.div>
  );
};

export default Modal;