import { useState } from 'react';
import { Button } from 'react-bootstrap';
import Accordion from 'react-bootstrap/Accordion';
import Form from 'react-bootstrap/Form';
import Spinner from 'react-bootstrap/Spinner';
import { uploadBills, uploadLegislators, uploadVoteResults, uploadVotes } from '../../services/api';


interface UploadSectionProps {
  title: string;
  onFileSelect: (file?: File) => void;
}

const UploadSection: React.FC<UploadSectionProps> = ({ title, onFileSelect }) => (
  <Accordion.Item eventKey={title}>
    <Accordion.Header>{title}</Accordion.Header>
    <Accordion.Body>
      <Form.Group controlId={`formFile-${title}`} className="mb-3">
        <Form.Control 
          type="file" 
          onChange={(e) => onFileSelect((e.target as HTMLInputElement).files?.[0])} 
        />
      </Form.Group>
    </Accordion.Body>
  </Accordion.Item>
);

const Uploads: React.FC = () => {
  const [files, setFiles] = useState<{ [key: string]: File | undefined }>({});
  const [isLoading, setIsLoading] = useState<boolean>(false);

  const handleFileSelect = (key: string) => (file?: File) => {
    setFiles((prevFiles) => ({ ...prevFiles, [key]: file }));
  };

  const handleUpload = async () => {
    setIsLoading(true);
  
    try {
      if (files.bills) {
        await uploadBills(files.bills);
      }
      if (files.legislators) {
        await uploadLegislators(files.legislators);
      }
      if (files.votes) {
        await uploadVotes(files.votes);
      }
      if (files.voteResults) {
        await uploadVoteResults(files.voteResults);
      }
    } catch (error) {
      console.error("Upload error:", error);
    } finally {
      setIsLoading(false);
    }
  };
  

  const uploadSections = [
    { key: "bills", title: "Select Bills File" },
    { key: "legislators", title: "Select Legislators File" },
    { key: "votes", title: "Select Votes File" },
    { key: "voteResults", title: "Select Vote Results File" }
  ];

  return (
    <Accordion defaultActiveKey="0">
      {isLoading ? 
        <Spinner animation="border" role="status">
          <span className="visually-hidden">Loading...</span>
        </Spinner>
        :
        <>
          {uploadSections.map(({ key, title }) => (
            <UploadSection 
              key={key} 
              title={title} 
              onFileSelect={handleFileSelect(key)} 
            />
          ))}
          <Button id='btn-upload' size='lg' onClick={handleUpload}>Upload Files</Button>  
        </>
      }
    </Accordion>
  );
};

export default Uploads;
