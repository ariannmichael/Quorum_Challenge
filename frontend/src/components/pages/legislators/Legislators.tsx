import React from 'react';
import { LegislatorBills } from '../../../models/LegislatorModels';
import { downloadLegislators, getLegislatorsBills } from '../../../services/api';
import { Button, Container } from 'react-bootstrap';
import './Legislators.css';
import LegislatorCard from './LegislatorCard';

const Legislators: React.FC = () => {
    const [legislatorsBills, setLegislatorsBills] = React.useState<LegislatorBills[]>();

    React.useEffect(() => {
        getLegislatorsBills().then((response) => {
            setLegislatorsBills(response.data);
        });
    }, []);

    const handleDownload = () => {
        downloadLegislators('legislators-support-oppose-count.csv');
    }

    return (
        <Container className='legislator-container'>
            <div className="legislator-header">
                <h1>Legislators</h1>
                <Button onClick={handleDownload}>Download CSV</Button>
            </div>
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