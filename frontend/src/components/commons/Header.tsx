import React from "react";
import { Container, Nav, Navbar } from "react-bootstrap";

const Header: React.FC = () => {
    return (
        <Navbar expand="lg" className="bg-body-secondary">
            <Container>
                <Navbar.Brand href="/">
                    <h3>Quorum Test</h3>
                </Navbar.Brand>
                <Navbar.Toggle aria-controls="basic-navbar-nav" />
                <Navbar.Collapse id="basic-navbar-nav">
                    <Nav className="ms-4">
                        <Nav.Link href="/">Home</Nav.Link>
                        <Nav.Link href="/legislators">Legislators</Nav.Link>
                        <Nav.Link href="/bills">Bills</Nav.Link>
                    </Nav>
                </Navbar.Collapse>
            </Container>
        </Navbar>
    );
}

export default Header;