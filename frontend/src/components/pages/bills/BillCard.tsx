import React from "react";
import { BillDetail } from "../../../models/BillModels";
import { Card } from "react-bootstrap";
import { FaThumbsUp, FaThumbsDown } from 'react-icons/fa';

interface BillCardProps {
    billDetail: BillDetail
}

const BillCard: React.FC<BillCardProps> = ({ billDetail }) => {
    return (
        <Card className='bill-card'>
            <Card.Body>
                <Card.Title><h3>{billDetail.bill.id} - {billDetail.bill.title}</h3></Card.Title>
                <Card.Text >
                    <hr></hr>
                    <div className="bill-card__description">
                        <div>
                            <h5>Primary Sponsor: {billDetail.bill.primary_sponsor}</h5> 
                        </div>
                        <div>
                            <h5 className="bill-card__supporters-opposers">
                                <FaThumbsUp color="green"/> &nbsp; Supporters: {billDetail.supporters}
                            </h5>
                        </div>
                        <div>
                            <h5 className="bill-card__supporters-opposers">
                                <FaThumbsDown color="red"/> &nbsp; Opposers: {billDetail.opposers}
                            </h5>
                        </div>
                    </div>
                </Card.Text>
            </Card.Body>
        </Card>
    );
}

export default BillCard;