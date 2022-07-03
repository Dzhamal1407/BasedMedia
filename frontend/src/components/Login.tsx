import React from 'react';
import {LockClosedIcon, UserIcon} from "@heroicons/react/outline";

const Login: React.FC = () => {
  return (
    <div className='w-11/12 px-[-20px] bg-zinc-800 rounded-2xl text-white modal:w-96'>

      <div className='text-3xl text-center py-6'>
        Log In
      </div>

      <form className='flex flex-col gap-10 mt-4 justify-center'>

        <div className='flex flex-col gap-2.5 px-10 w-full'>
            <label className='text-base'>Email or Username</label>
            <div className='flex bg-zinc-700 h-11 rounded-lg text-xl'>
              <UserIcon className="w-6 mx-4 text-gray-900"/>
              <input className='bg-inherit border-none text-base
               focus:outline-none' type="text"/>
            </div>

        </div>

        <div className='flex flex-col gap-2.5 px-10 w-full'>
            <label className='text-base'>Password</label>
            <div className='flex bg-zinc-700 h-11 rounded-lg text-xl'>
              <LockClosedIcon className="w-6 mx-4 text-gray-900"/>
              <input className='bg-inherit border-none text-base
               focus:outline-none placeholder-opacity-50 text-white' type="password"/>
            </div>
        </div>

        <input className='w-48 py-1 bg-blue-700 rounded-3xl place-self-center text-lg' type="submit" value='Login'/>

      </form>

      <div>
        <p className='opacity-70'>Don&apos;t have an account? <span className='text-indigo-500'>Sign Up!</span></p>
      </div>

    </div>
  );
};

export default Login;