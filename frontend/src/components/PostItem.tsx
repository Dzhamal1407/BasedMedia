import React from 'react';
import {IPost} from '../types/post'
import Image from "next/image";

interface PostItemProps {
  post: IPost;
}

const PostItem: React.FC<PostItemProps> = ({post}) => {
  return (
    <div className='flex flex-col w-full bg-zinc-800 text-white'>
      <div>
        {post.content}
      </div>
      <div className='relative self-center w-[528px] flex items-center h-96'>
        <Image
          src={'http://127.0.0.1:8000/static/' + post.image}
          objectFit={'contain'}
          layout={'fill'}
          alt={''}
        />
      </div>

    </div>
  );
};

export default PostItem;