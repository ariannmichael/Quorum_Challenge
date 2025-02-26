import React from "react";
import { Card } from "react-bootstrap";
import { LegislatorBills } from "../../../models/LegislatorModels";
import { FaThumbsDown, FaThumbsUp } from "react-icons/fa";

interface LegislatorCardProps {
    legislatorBills: LegislatorBills
}

const LegislatorCard: React.FC<LegislatorCardProps> = ({ legislatorBills }) => {
    return (
        <Card className='legislator-card'>
            <Card.Body>
                <Card.Title><h3>{legislatorBills.legislator.id} - {legislatorBills.legislator.name}</h3></Card.Title>
                <Card.Text >
                    <hr></hr>
                    <div className="legislator-card__description">
                        <div>
                            <h5 className="legislator-card__supported-opposed">
                                <FaThumbsUp color="green"/> &nbsp; Supported Bills: {legislatorBills.supported_bills}
                            </h5>
                        </div>
                        <div>
                            <h5 className="legislator-card__supported-opposed">
                                <FaThumbsDown color="red"/> &nbsp; Opposed Bills: {legislatorBills.opposed_bills}
                            </h5>
                        </div>
                    </div>
                </Card.Text>
            </Card.Body>
        </Card>
    );
}

export default LegislatorCard;