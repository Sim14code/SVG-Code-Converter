import React, { useState } from "react";
import {
  ApolloClient,
  InMemoryCache,
  ApolloProvider,
  useMutation,
  gql,
} from "@apollo/client";

const UPLOAD_IMAGE = gql`
  mutation UploadImage($file: Upload!) {
    uploadImage(file: $file) {
      id
      svg
    }
  }
`;

const client = new ApolloClient({
  uri: "http://localhost:8000/graphql",
  cache: new InMemoryCache(),
});

function UploadFormInner() {
  const [file, setFile] = useState(null);
  const [svg, setSvg] = useState(null);
  const [uploadImage] = useMutation(UPLOAD_IMAGE, {
    onCompleted: (data) => setSvg(data.uploadImage.svg),
  });

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!file) return;

    uploadImage({ variables: { file } });
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input
          type="file"
          accept="image/*"
          onChange={(e) => setFile(e.target.files[0])}
        />
        <button type="submit">Convert</button>
      </form>
      {svg && (
        <div>
          <h3>Resulting SVG:</h3>
          <div dangerouslySetInnerHTML={{ __html: svg }} />
        </div>
      )}
    </div>
  );
}

export default function UploadForm() {
  return (
    <ApolloProvider client={client}>
      <UploadFormInner />
    </ApolloProvider>
  );
}
