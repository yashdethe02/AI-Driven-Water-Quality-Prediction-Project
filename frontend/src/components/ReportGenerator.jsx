import { PDFDownloadLink } from '@react-pdf/renderer';
import ResearchReport from './ResearchReport';

const ReportGenerator = ({ data }) => (
  <PDFDownloadLink
    document={<ResearchReport data={data} />}
    fileName="water_analysis.pdf"
  >
    {({ loading }) => (
      <button disabled={loading}>
        {loading ? 'Generating Report...' : 'Download PDF Report'}
      </button>
    )}
  </PDFDownloadLink>
);