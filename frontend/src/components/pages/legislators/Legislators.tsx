import React from 'react';
import { LegislatorBills } from '../../../models/LegislatorModels';
import { getLegislatorsBills } from '../../../services/api';
import { Container } from 'react-bootstrap';
import './Legislators.css';
import LegislatorCard from './LegislatorCard';

const Legislators: React.FC = () => {
    const [legislatorsBills, setLegislatorsBills] = React.useState<LegislatorBills[]>();

    React.useEffect(() => {
        getLegislatorsBills().then((response) => {
            setLegislatorsBills(response.data);
        });
    }, []);

    return (
        <Container className='legislator-container'>
            <h1>Legislators</h1>
            <div className='legislators-wrapper'>
                {legislatorsBills && legislatorsBills.length === 0 && <h2>No legislators found</h2>}
                {legislatorsBills?.map((legislatorBill) => (
                    <LegislatorCard key={legislatorBill.legislator.id} legislatorBills={legislatorBill} />
                ))}
            </div>
        </Container>
    );
}

export default Legislators;