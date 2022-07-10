import React, {useState} from 'react';
import {ChevronDownIcon, CubeTransparentIcon, FireIcon, UserIcon} from "@heroicons/react/outline";
import Search from "./Search";
import Modal from "./Modal";
import Login from "./Login";
import {AnimatePresence} from "framer-motion";

const Header: React.FC = () => {

  const [authModalActive, setAuthModalActive] = useState(false)

  return (

    <>
      <div className='flex fixed z-10 place-content-center bg-zinc-800 h-14 w-full'>

        <div className='inline-flex gap-4 text-white items-center w-full max-w-5xl'>
           <div className='flex ml-3 gap-1 text-2xl italic'>
            <CubeTransparentIcon className='w-7'/>
            <p className='md:hidden'>BM</p>
            <p className='hidden md:inline'>BasedMedia</p>
            <FireIcon className='w-7'/>
          </div>
          <Search/>
          <button
            className='hidden bg-indigo-600 rounded-3xl py-1 px-6 hover:brightness-125 md:inline'
            onClick={() => setAuthModalActive(true)}
          >
            Sing In
          </button>
          <div className='inline-flex mr-3 cursor-pointer outline-offset-2 outline-gray-600 hover:outline hover:outline-1'>
            <UserIcon className='w-6 basis-8 stroke-1 text-white flex-none'/>
            <ChevronDownIcon className='w-6 text-white'/>
          </div>
        </div>

      </div>

      <AnimatePresence
        initial={false}
        exitBeforeEnter={true}
        onExitComplete={() => null}
      >
        {authModalActive && <Modal active={authModalActive} setActive={setAuthModalActive}>
          <Login/>
        </Modal>}
      </AnimatePresence>
  </>
  );
};

export default Header;