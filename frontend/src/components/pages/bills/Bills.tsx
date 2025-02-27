import React from 'react';
import { BillDetail } from '../../../models/BillModels';
import { downloadBills, getBillsDetails } from '../../../services/api';
import { Button, Container } from 'react-bootstrap';
import './Bills.css';
import BillCard from './BillCard';

const Bills: React.FC = () => {
    const [bills, setBills] = React.useState<BillDetail[]>();

    React.useEffect(() => {
        getBillsDetails().then((response) => {
            setBills(response.data);
        });
    }, []);

    const handleDownload = () => {
        downloadBills('bills.csv');
    }

    return (
        <Container className='bill-container'>
            <div className="bills-header">
                <h1>Bills</h1>
                <Button onClick={handleDownload}>Download CSV</Button>
            </div>
            <div className='bills-wrapper'>
                {bills && bills.length === 0 && <h2>No bills found</h2>}
                {bills?.map((bill) => (
                    <BillCard key={bill.bill.id} billDetail={bill} />
                ))}
            </div>
        </Container>
    );
}

export default Bills;