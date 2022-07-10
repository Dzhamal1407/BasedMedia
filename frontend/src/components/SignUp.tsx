import React from 'react';
import {LockClosedIcon, UserIcon} from "@heroicons/react/outline";

const SignUp = () => {
  return (
    <>

      <div className='text-3xl text-center py-8'>
        Log In
      </div>

      <form className='flex flex-col gap-8 px-8 justify-center'>

        <div className='flex flex-col gap-2.5 w-full'>
            <label className='text-base'>Email or Username</label>
            <div className='focus-within:outline focus-within:outline-2
             focus-within:outline-blue-700 flex items-center gap-3.5 bg-zinc-700 h-11 rounded-lg'>
              <UserIcon className="w-7 ml-3.5 text-gray-900"/>
              <input
                className='bg-inherit text-base w-4/5 mr-3.5 outline-none'
                type="text"
                placeholder='Enter your email or username'
              />
            </div>

        </div>

        <div className='flex flex-col gap-2.5 w-full'>
            <label className='text-base'>Password</label>
            <div className='focus-within:outline focus-within:outline-2 focus-within:outline-blue-700 flex items-center gap-3.5 bg-zinc-700 h-11 rounded-lg'>
              <LockClosedIcon className="w-7 ml-3.5 text-gray-900"/>
              <input
                className='bg-inherit text-base w-4/5 mr-3.5 outline-none'
                type="password"
                placeholder='Enter your password'/>
            </div>
        </div>

        <input className='w-48 my-1 py-1 bg-blue-700 rounded-3xl place-self-center text-lg' type="submit" value='Login'/>

      </form>

      <div className='text-center py-7 text-lg'>
        <p className='text-gray-300'>
          Don&apos;t have an account? <span className='text-indigo-500'>Sign Up!</span>
        </p>
      </div>

    </>
  );
};

export default SignUp;