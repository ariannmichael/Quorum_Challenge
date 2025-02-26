import React from 'react';
import { BillDetail } from '../../../models/BillModels';
import { getBillsDetails } from '../../../services/api';
import { Container } from 'react-bootstrap';
import './Bills.css';
import BillCard from './BillCard';

const Bills: React.FC = () => {
    const [bills, setBills] = React.useState<BillDetail[]>();

    React.useEffect(() => {
        getBillsDetails().then((response) => {
            setBills(response.data);
        });
    }, []);

    return (
        <Container className='bill-container'>
            <h1>Bills</h1>
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