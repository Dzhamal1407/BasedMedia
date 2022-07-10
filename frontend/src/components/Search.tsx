import React from 'react';
import {SearchIcon} from "@heroicons/react/outline";

const Search = () => {
  return (
    <div className='flex gap-3 align-center bg-zinc-700 grow h-9 rounded-lg hover:drop-shadow-lg max-w-xl'>
      <SearchIcon className='w-5 ml-3 text-indigo-600'/>
      <input className='bg-inherit outline-none w-10 mr-4 grow' type="text" placeholder='Search'/>
    </div>
  );
};

export default Search;