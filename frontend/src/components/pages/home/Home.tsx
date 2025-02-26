import React from 'react';
import { Button, Container } from 'react-bootstrap';
import { FaPerson } from "react-icons/fa6";
import { FaBook } from "react-icons/fa";
import './Home.css';
import Uploads from '../../commons/Uploads';

const Home: React.FC = () => {
    return (
        <Container className='home-container'>
            <div className='home-wrapper'>
                <Button href="/legislators" size='lg'>
                    <div>
                        <FaPerson size={72}/> 
                        <br/>
                        Legislators
                    </div>
                </Button>
                <Button href="/bills" size='lg'>
                    <FaBook size={72}/> 
                    <br/>
                    Bills
                </Button>
            </div>
            <div className="home-uploads">
                <Uploads/>
            </div>
        </Container>
    );
}

export default Home;